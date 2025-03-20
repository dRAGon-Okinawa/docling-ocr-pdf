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
        pipeline: str = Input(
            description="Pipeline to process PDF or image files", default="standard", choices=["standard", "vlm"]),
        vlm_model: str = Input(
            description="VLM model to use (only for VLM pipeline)", default="smoldocling", choices=["", "smoldocling", "granite_vision"]),
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
        
        # Specify the pipeline to use
        docling_args.extend(["--pipeline", pipeline])

        # Arguments based on the pipeline
        if pipeline == "vlm":
            # Throw an error if the VLM model is not specified
            if vlm_model == "":
                raise ValueError(
                    "VLM model must be specified when using the VLM pipeline")
            docling_args.extend(["--vlm-model", vlm_model])

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
                output_files.append(Path(file))

        # Return the output files
        return output_files
