# Copyright 2017 QuantRocket - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def add_subparser(subparsers):
    _parser = subparsers.add_parser("countdown", description="QuantRocket cron service CLI", help="quantrocket countdown -h")
    _subparsers = _parser.add_subparsers(title="subcommands", dest="subcommand")
    _subparsers.required = True

    parser = _subparsers.add_parser("crontab", help="upload a new crontab, or return the current crontab")
    parser.add_argument("service", metavar="SERVICE_NAME", help="the name of the countdown service, e.g. countdown-usa")
    parser.add_argument("-f", "--filename", metavar="FILENAME", help="the crontab file to upload (if omitted, return the current crontab)")
    parser.set_defaults(func="quantrocket.countdown._load_or_show_crontab")

    parser = _subparsers.add_parser("timezone", help="show the countdown service timezone")
    parser.add_argument("service", metavar="SERVICE_NAME", help="The name of the countdown service, e.g. countdown-usa")
    parser.set_defaults(func="quantrocket.countdown._cli_get_timezone")
