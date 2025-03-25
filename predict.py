# https://cog.run/python
import subprocess
import uuid
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        # Anything to load here?

    def predict(
        self,
        document: Path = Input(description="Document to process"),
        from_format: str = Input(
            description="Input document format", default="any", choices=["any", "docx", "pptx", "html", "image", "pdf", "asciidoc", "md", "csv", "xlsx", "xml_uspto", "xml_jats", "json_docling"]),
        to_format: str = Input(
            description="Output document format", default="md", choices=["md", "json", "html", "text", "doctags"]),
        timeout: int = Input(
            description="Maximum time allowed to run the prediction in seconds", default=120, ge=30, le=3600)
    ) -> list[Path]:
        """Run a single prediction on the model"""
        print("Docling will work on :", document)

        # Create the output directory
        output_dir = "/tmp/docling_output"
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        print("Docling will output files to :", output_dir)

        # Clean all files (if any) in the output directory
        print("Cleaning the output directory...")
        for file in Path(output_dir).iterdir():
            if file.is_file():
                file.unlink()

        # Prepare docling arguments
        docling_args = [
            "docling",
            "--to", to_format,
            "--image-export-mode", "placeholder",
            "--document-timeout", str(timeout),
            "--output", output_dir,
            "--artifacts-path", "/opt/docling/models"
        ]
        
        # Append from_format argument if not "any"
        if from_format != "any":
            docling_args.extend(["--from", from_format])

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
        for file in Path(output_dir).iterdir():
            if file.is_file():
                # Rename file using UUID
                new_name = str(uuid.uuid4()) + file.suffix
                file.rename(file.with_name(new_name))
                output_files.append(Path(file.with_name(new_name)))

        # Print the output files
        print("Output files are :", output_files)
        
        # If no output files are found, raise an exception
        if len(output_files) == 0:
            raise Exception("No output files found!")

        # Print see you later
        print("See you later!")

        # Return the output files
        return output_files
