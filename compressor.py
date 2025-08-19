import numpy as np
from sklearn.decomposition import PCA
import zlib
import pickle

BLOCK_SIZE = 32      # Change as needed
COMP_DIM = 16        # Compressed size per block

def file_to_blocks(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    # Pad so it's a multiple of BLOCK_SIZE
    if len(data) % BLOCK_SIZE != 0:
        data += bytes([0]) * (BLOCK_SIZE - len(data)%BLOCK_SIZE)
    blocks = [data[i:i+BLOCK_SIZE] for i in range(0, len(data), BLOCK_SIZE)]
    return np.array([np.frombuffer(b, dtype=np.uint8) for b in blocks])

def compress(input_file, output_file, pca_file):
    X = file_to_blocks(input_file)
    pca = PCA(n_components=COMP_DIM)
    X_comp = pca.fit_transform(X)
    # Quantize
    X_comp_q = np.rint(X_comp).astype(np.int16)
    # Serialize compressed data and PCA
    with open(pca_file, 'wb') as f:
        pickle.dump(pca, f)
    c_stream = zlib.compress(X_comp_q.tobytes())
    with open(output_file, 'wb') as f:
        f.write(c_stream)

if __name__ == "__main__":
    compress('test.txt', 'quantum_compressed.bin', 'pca_model.pkl')
