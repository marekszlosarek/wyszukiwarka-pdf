import os
from PyPDF2 import PdfReader

def search_text_in_pdfs(folder_path, search_string) -> str:
    pdf_files = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')],
        key=lambda f: os.path.getmtime(os.path.join(folder_path, f)),
        reverse=True
    )

    for i, pdf_file in enumerate(pdf_files):
        file_path = os.path.join(folder_path, pdf_file)
        
        if i%100 == 0:
            print(f"Sprawdzono {i}/{len(pdf_files)} dostępnych programów.")
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                if search_string.lower() in page.extract_text().lower():
                    print(f"Sprawdzono {i+1}/{len(pdf_files)} dostępnych programów.")
                    return pdf_file
        except Exception as e:
            print(f"Błąd wczytując {pdf_file}: {e}")

    print("Nie znaleziono detalu.")
    return None


if __name__ == "__main__":
    folder = input("Podaj ścieżkę do folderu z programami: ")
    text_to_find = input("Wpisz SN do wyszukania: ")
    print()
    
    result = search_text_in_pdfs(folder, text_to_find)
    if result:
        print(f"\nDetal znaleziono w: {result}")
    else:
        print("\nNie znaleziono detalu.")
    input("\nWciśnij Enter, żeby zamknąć... ")
    
