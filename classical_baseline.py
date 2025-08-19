import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    compressed = zlib.compress(data)
    with open(output_file, 'wb') as f:
        f.write(compressed)

def decompress_file(compressed_file, output_file):
    with open(compressed_file, 'rb') as f:
        data = f.read()
    decompressed = zlib.decompress(data)
    with open(output_file, 'wb') as f:
        f.write(decompressed)

if __name__ == "__main__":
    compress_file('test.txt', 'compressed_classical.z')
    decompress_file('compressed_classical.z', 'decompressed_classical.txt')
