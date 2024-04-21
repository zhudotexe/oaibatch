import argparse
import sys

from . import cancel, list, main
from ._version import __version__

# create the top-level parser and add subcommands
parser = argparse.ArgumentParser()
parser.add_argument("--version", action="version", version=f"oaibatch {__version__} on Python {sys.version}")
subparsers = parser.add_subparsers(title="subcommands")

# main args
parser.add_argument("file", type=argparse.FileType("r"), help="the file to submit as a batch request")
parser.set_defaults(entrypoint=main.entrypoint)

# --- subparsers ---
# list
parser_list = subparsers.add_parser("list", aliases=["ls"], help="list all running batch jobs in the organization")
parser_list.set_defaults(entrypoint=list.entrypoint)

# cancel
parser_cancel = subparsers.add_parser("cancel", aliases=["rm"], help="cancel a running batch job")
parser_cancel.add_argument("jobid", help="the id of the job to cancel")
parser_cancel.set_defaults(entrypoint=cancel.entrypoint)

# parse and run correct entrypoint
args = parser.parse_args()
args.entrypoint(args)
