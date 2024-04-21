# oaibatch

A simple command-line tool to run batch completions against the OpenAI API.

This tool can be used to submit batch jobs to the OpenAI API and to notify you when they are completed. In more detail,
this tool:

<!-- TODO
- Validates that your requests are valid by:
    - checking the file against the known spec
    - sampling 3 random requests against the (non-batch) API
-->

- Uploads the batch file to the API
- Submits the batch job
- Periodically checks in to test for job completion
- Downloads the completion and error files (default: `JOBID_output.jsonl` and `JOBID_error.jsonl`)
- Emails you to notify completion (see *email configuration* below)
- Cleans up the uploaded batch file

## Installation

Requires Python 3.8+.

```shell
$ pip install git+https://github.com/zhudotexe/oaibatch.git@main
```

## Usage

You must set the `OPENAI_API_KEY` environment variable.

To control the organization requests are made in, use the `OPENAI_ORG_ID` environment variable.

```shell
# submit a batch job
$ oaibatch my_jsonl_batch_file.jsonl

# list ongoing batch jobs
$ oaibatch list

# cancel a batch job
$ oaibatch cancel <job_id>

# view a list of all commands
$ oaibatch --help
```

## Email Configuration

To configure `oaibatch` to send emails on completion, your system must set up the `mail` command. By default,
`oaibatch` will use `mail` to send the results of the batch job to the current user, and attach the input and generated
files.


## TODO

- [ ] `-i` interactive mode, estimate cost and ask
- [ ] `-q` no emails
- [ ] configure email recipient
- [ ] configure output files
- [ ] configure completion check rate
