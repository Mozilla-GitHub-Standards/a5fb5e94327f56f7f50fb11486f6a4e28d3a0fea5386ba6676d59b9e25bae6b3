# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Signing Service
#
# The Initial Developer of the Original Code is the Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Ryan Tilder (rtilder@mozilla.com)
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

"""Main entry point
"""
import crypto


def includeme(config):
    # authorization
    #config.include('pyramid_ipauth')

    config.include("cornice")

    config.scan("signing.views")

    crypto.init(key=config.registry.settings['signing.keyfile'],
                cert=config.registry.settings['signing.certfile'])

    issuers = config.registry.settings.get('signing.permitted_issuers', '')
    issuers = issuers.split(',')
    iss = []
    for issuer in issuers:
        iss.append(issuer.strip())
    if len(iss) < 1:
        raise Exception("No issuers provided in the config file!")
    config.registry.settings['signing.permitted_issuers'] = iss


def main(global_config, **settings):
    from mozsvc.config import get_configurator
    config = get_configurator(global_config, **settings)
    config.include(includeme)
    return config.make_wsgi_app()
