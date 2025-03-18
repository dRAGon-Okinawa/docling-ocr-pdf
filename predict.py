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
        timeout: int = Input(description="Maximum time allowed to run the prediction in seconds", default=120, ge=30, le=3600)
    ) -> Path:
        """Run a single prediction on the model"""
        # Retrieve document name and extension
        document_name = document.stem
        # Replace (any) extension to .md :
        output_document = "/opt/docling/output/" + document_name + ".md"
        print("Docling will work on :", document)
        print("Docling will output to :", output_document)

        # Launch command (system call)
        subprocess.run(
            ["docling", "--artifacts-path", "/opt/docling/models", "--from", "pdf", "--to", "md", "--image-export-mode", "placeholder", "--table-mode", "accurate", "--output", "/opt/docling/output", document],
            timeout=timeout,  # Set the timeout in seconds
            check=True  # Raise exception if the command returns a non-zero exit code
        )
    
        # Return the output path
        return Path(output_document)
