import numpy as np
from sklearn.decomposition import PCA
import zlib
import pickle

BLOCK_SIZE = 32
COMP_DIM = 16

def decompress(compressed_file, pca_file, output_file):
    with open(pca_file, 'rb') as f:
        pca = pickle.load(f)
    with open(compressed_file, 'rb') as f:
        c_stream = f.read()
    data_q = np.frombuffer(zlib.decompress(c_stream), dtype=np.int16)
    # reshape: number of blocks x COMP_DIM
    n_blocks = data_q.size // COMP_DIM
    X_comp_q = data_q.reshape((n_blocks, COMP_DIM))
    X_rec = pca.inverse_transform(X_comp_q)
    X_rec_uint = np.clip(np.rint(X_rec), 0, 255).astype(np.uint8)
    bytes_data = b''.join([row.tobytes() for row in X_rec_uint])
    with open(output_file, 'wb') as f:
        f.write(bytes_data.rstrip(b'\x00'))   # remove padding

if __name__ == "__main__":
    decompress('quantum_compressed.bin', 'pca_model.pkl', 'decompressed_quantum.txt')
