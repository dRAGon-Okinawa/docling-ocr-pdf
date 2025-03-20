# docling-ocr-pdf
> The **docling-ocr-pdf** model utilizes the document processing capabilities from the [Docling](https://github.com/docling-project/docling) project to perform Optical Character Recognition (OCR) on a variety of document formats, including but not limited to PDFs. 
> 
> It enables efficient document preprocessing, making textual data ready for generative AI tasks. 
> 
> This model is independently accessible via [Replicate.com](https://replicate.com/dragon-okinawa/docling-ocr-pdf) to ensure easy use and deployment.

## Features
- **OCR Capabilities**: Transforms various document formats into machine-readable text using advanced OCR techniques.
- **Leverages Docling**: Utilizes Docling's powerful document parsing capabilities but operates independently, simplifying deployment.
- **Accessible via Replicate**: Available on [Replicate.com](https://replicate.com/dragon-okinawa/docling-ocr-pdf), which facilitates straightforward deployment and integration into workflows.
- **Versatile Integration**: Compatible with AI workflows, offering a comprehensive solution for text extraction across multiple document types.


## Development
### Install cog
```bash
sudo curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_`uname -s`_`uname -m`
sudo chmod +x /usr/local/bin/cog
```

### Check if cog can run
```bash
cog run python
```

### Test prediction
```bash
cog predict -i document=@tests/resources/Optical_character_recognition.pdf
```

## Deploy to Replicate
```bash
cog login
cog build --tag r8.im/dragon-okinawa/docling-ocr-pdf:latest
cog push r8.im/dragon-okinawa/docling-ocr-pdf
```