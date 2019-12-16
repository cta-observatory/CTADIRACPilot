__RCSID__ = "$Id$"

import os


from pilotTools import CommandBase


class CTASetEnv(CommandBase):
  """ Set custom CTA environment
  """

  def execute(self):
    """ Standard method for pilot commands
    """

    self.pp.installEnv['DIRACSYSCONFIG'] = os.path.join(os.environ['DIRAC'],'pilot.cfg')
