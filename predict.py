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
            description="Input document format", default="pdf", choices=["docx", "pptx", "html", "image", "pdf", "asciidoc", "md", "csv", "xlsx", "xml_uspto", "xml_jats", "json_docling"]),
        to_format: str = Input(
            description="Output document format", default="md", choices=["md", "json", "html", "text", "doctags"]),
        timeout: int = Input(
            description="Maximum time allowed to run the prediction in seconds", default=120, ge=30, le=3600)
    ) -> list[Path]:
        """Run a single prediction on the model"""
        print("Docling will work on :", document)
        print("Docling will output to : /opt/docling/output")

        # Prepare docling arguments :
        docling_args = [
            "docling",
            "--from", from_format,
            "--to", to_format,
            "--image-export-mode", "placeholder",
            "--document-timeout", str(timeout),
            "--output", "/opt/docling/output",
            "--artifacts-path", "/opt/docling/models"
        ]

        # Append document argument
        docling_args.append(document)

        # Show the docling command and arguments
        print("Docling command to be used :", docling_args)

        # Print that we are starting the docling command
        print("Starting docling...")

        # Launch docling command (system call)
        subprocess.run(
            docling_args,
            timeout=timeout,  # Command timeout in seconds
            check=True  # Raise exception if the command returns a non-zero exit code
        )

        # Searching for the output files inside the output directory
        output_files = []
        for file in Path("/opt/docling/output").iterdir():
            if file.is_file():
                # If file contains a space in its name, replace it with an underscore
                if " " in file.name:
                    new_name = file.name.replace(" ", "_")
                    file.rename(file.with_name(new_name))
                    output_files.append(Path(file.with_name(new_name)))
                else:
                    output_files.append(Path(file))

        # Return the output files
        return output_files
