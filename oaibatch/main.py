import logging
from typing import TextIO

from openai import OpenAI

log = logging.getLogger("oaibatch")


class Main:
    def __init__(self):
        self.client = OpenAI()

    def run(self, f: TextIO):
        # TODO: validate file

        # - Uploads the batch file to the API
        batch_file = self.upload_file(f)

        # - Submits the batch job
        job = self.client.batches.create(
            input_file_id=batch_file.id,
            completion_window="24h",
            endpoint="/v1/chat/completions",
        )

        # - Periodically checks in to test for job completion
        # - Downloads the completion and error files (default: `JOBID_output.jsonl` and `JOBID_error.jsonl`)
        # - Emails you to notify completion (see *email configuration* below)
        # - Cleans up the uploaded batch file

    def upload_file(self, f):
        result = self.client.files.create(file=f, purpose="batch")
        log.info(f"Uploaded file {result.id} (size={result.bytes})")
        return result


def entrypoint(args):
    runner = Main()
    runner.run(f=args.file)
