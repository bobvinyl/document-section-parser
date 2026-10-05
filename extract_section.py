import docx

def extract_section_from_docx(docx_path, section_heading, next_heading):
    doc = docx.Document(docx_path)
    section_text = []
    capture = False
    
    for paragraph in doc.paragraphs:
        # Check if we hit our target header
        if paragraph.text.strip().lower() == section_heading.lower():
            capture = True
            continue
        
        # Stop capturing if we hit the next section heading
        if capture and paragraph.text.strip().lower() == next_heading.lower():
        #if capture and paragraph.style.name.startswith('Heading'):
            break
            
        if capture:
            section_text.append(paragraph.text)
            
    return "\n".join(section_text)

# Usage
section = extract_section_from_docx("input/section_test.docx", "Section 1", "Section 2")
print(section)