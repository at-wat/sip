# Copyright (c) 2019, Riverbank Computing Limited
# All rights reserved.
#
# This copy of SIP is licensed for use under the terms of the SIP License
# Agreement.  See the file LICENSE for more details.
#
# This copy of SIP may also used under the terms of the GNU General Public
# License v2 or v3 as published by the Free Software Foundation which can be
# found in the files LICENSE-GPL2 and LICENSE-GPL3 included in this package.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from ..argument_parser import ArgumentParser
from ..exceptions import handle_exception

from .distinfo import distinfo


def main():
    """ Create and populate a .dist-info directory. """

    # Parse the command line.
    parser = ArgumentParser("Create and populate a .dist-info directory.")

    parser.add_argument('--console-script', dest='console_scripts',
            action='append', help="the entry point of a console script",
            metavar='ENTRY-POINT')

    parser.add_argument('--generator',
            help="the name of the program generating the directory",
            metavar="NAME")

    parser.add_argument('--inventory', required=True,
            help="the file containing the names of the files in the project",
            metavar="FILE")

    parser.add_argument('--prefix', help="the installation prefix directory",
            metavar="DIR")

    parser.add_argument('--project-root',
            help="the directory containing pyproject.toml", metavar="DIR")

    parser.add_argument('--requires-dist', help="additional Requires-Dist",
            metavar="EXPR")

    parser.add_argument('--wheel-tag',
            help="the tag if a wheel is being created", metavar="TAG")

    parser.add_argument(dest='names', nargs=1,
            help="the name of the .dist-info directory", metavar='directory')

    args = parser.parse_args()

    try:
        distinfo(name=args.names[0], console_scripts=args.console_scripts,
                generator=args.generator, inventory=args.inventory,
                prefix=args.prefix, project_root=args.project_root,
                requires_dist=args.requires_dist, wheel_tag=args.wheel_tag)
    except Exception as e:
        handle_exception(e)

    return 0
