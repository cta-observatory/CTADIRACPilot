__RCSID__ = "$Id$"

import os

from pilotCommands import GetPilotVersion, \
    InstallDIRAC, \
    ConfigureBasics, \
    ConfigureCPURequirements, \
    ConfigureSite, \
    ConfigureArchitecture

from pilotTools import CommandBase

class CTACommandBase(CommandBase):
  """ Simple extension, just for LHCb parameters
  """

  def __init__(self, pilotParams):
    """ c'tor
    """
    super(CTACommandBase, self).__init__(pilotParams)
    pilotParams.pilotCFGFile = 'pilot.json'
    pilotParams.localConfigFile = 'pilot.cfg'
    pilotParams.architectureScript = 'dirac-architecture'


class CTAGetPilotVersion(CTACommandBase, GetPilotVersion):
  """ Base is enough (pilotParams.pilotCFGFile = 'LHCb-pilot.json')
  """
  pass

class CTAConfigureArchitecture(CTACommandBase, ConfigureArchitecture):
  """ just sets the CMTCONFIG variable
  """

  def execute(self):
    """ calls the superclass execute and then sets the CMTCONFIG variable with the host binary tag
    """

    # This sets the DIRAC architecture
    super(CTAConfigureArchitecture, self).execute()

