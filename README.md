# docling-ocr-pdf
Docling Replicate Model : Get your documents ready for gen AI

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
cog push r8.im/dragon-okinawa/docling-ocr-pdf
```