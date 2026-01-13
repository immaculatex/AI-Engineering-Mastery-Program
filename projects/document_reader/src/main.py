from pipeline import process_document

chunks = process_document("sample.pdf")

for i, chunk in enumerate(chunks[:5]):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)
