# This file is part party_accise module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import party

def register():
    Pool.register(
        party.Party,
        party.PartyIdentifier,
        module='party_accise', type_='model')
