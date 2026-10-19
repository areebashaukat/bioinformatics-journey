from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

# --- PART 1: Sequence Metrics & Central Dogma ---
print("--- 1. Local Sequence Analysis ---")
my_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print("DNA Sequence:", my_dna)
print("Length:", len(my_dna), "bp")

# GC Content Calculation
seq_str = str(my_dna)
gc_content = ((seq_str.count('G') + seq_str.count('C')) / len(seq_str)) * 100
print(f"GC Content: {gc_content:.2f}%")

# Transcription & Translation
print("Transcribed RNA:", my_dna.transcribe())
print("Translated Protein:", my_dna.translate())


# --- PART 2: Fetching from NCBI using an Accession ID ---
print("\n--- 2. NCBI Entrez Online Fetch ---")
Entrez.email = "areeba@example.com"  # Replace with your actual email

target_id = "NC_000913.3"
print(f"Fetching accession ID: {target_id} from NCBI...")

try:
    handle = Entrez.efetch(db="nucleotide", id=target_id, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    
    print("Fetched Description:", record.description)
    print("Fetched Sequence Length:", len(record.seq), "bp")
    print("First 50 Bases:", record.seq[:50])
except Exception as e:
    print("Skipped online fetch (check internet connection):", e)


# --- PART 3: GenBank Annotation Parsing ---
print("\n--- 3. GenBank Record Parsing ---")
print("Downloading sample GenBank record (J01659.1)...")

try:
    handle_gb = Entrez.efetch(db="nucleotide", id="J01659.1", rettype="gb", retmode="text")
    gb_record = SeqIO.read(handle_gb, "genbank")
    handle_gb.close()

    print("Organism Name:", gb_record.annotations.get("organism", "Unknown"))
    print("Total Features found:", len(gb_record.features))
except Exception as e:
    print("Skipped GenBank fetch (check internet connection):", e)

print("\n--- Script Complete! ---")