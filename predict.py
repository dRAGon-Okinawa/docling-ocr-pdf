# https://cog.run/python
import subprocess
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        # Anything to load here?

    def predict(
        self,
        document: Path = Input(description="Document to process"),
        from_format: str = Input(
            description="Input format of the document", default="pdf", choices=["docx", "pptx", "html", "image", "pdf", "asciidoc", "md", "csv", "xlsx", "xml_uspto", "xml_jats", "json_docling"]),
        to_format: str = Input(
            description="Output format of the document", default="md", choices=["md", "json", "html", "text", "doctags"]),
        timeout: int = Input(
            description="Maximum time allowed to run the prediction in seconds", default=120, ge=30, le=3600)
    ) -> list[Path]:
        """Run a single prediction on the model"""
        print("Docling will work on :", document)
        print("Docling will output to : /opt/docling/output")

        # Launch command (system call)
        subprocess.run(
            [
                "docling",
                "--artifacts-path", "/opt/docling/models",
                "--from", from_format,
                "--to", to_format,
                "--image-export-mode", "placeholder",
                "--document-timeout", timeout,
                "--output", "/opt/docling/output",
                document
            ],
            timeout=timeout,  # Command timeout in seconds
            check=True  # Raise exception if the command returns a non-zero exit code
        )
        
        # Searching for the output files inside the output directory
        output_files = []
        for file in Path("/opt/docling/output").iterdir():
            if file.is_file():
                output_files.append(Path(file))
                
        # Return the output files
        return output_files
