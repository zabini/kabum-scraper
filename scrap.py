import os, logging, settings
from categories import Categories

logging.info('Starting scrap...')
cat = Categories()

cat.iterate()

logging.info('Ending scrap...')
