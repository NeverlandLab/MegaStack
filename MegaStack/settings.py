from pathlib import Path
import os

import dotenv
from split_settings.tools import optional, include

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
BASE_DIR = Path(__file__).resolve().parent.parent

include('core_settings/*.py')

DATABASE_ENGINE = os.environ.get("DATABASE_ENGINE", '')
if DATABASE_ENGINE != '':
    include('database_settings/' + DATABASE_ENGINE + ".py")
