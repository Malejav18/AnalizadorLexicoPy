# Diccionario de librerías y sus palabras reservadas
palabras_reservadas_librerias = {
    # Módulo math
    'math': {'pi', 'e', 'tau', 'inf', 'nan', 'sqrt', 'ceil', 'floor', 'trunc', 'pow', 'exp', 'log', 
             'log10', 'log2', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2', 'degrees', 
             'radians', 'hypot', 'factorial', 'gcd', 'lcm', 'isfinite', 'isinf', 'isnan'},

    # Módulo os
    'os': {'path', 'getenv', 'chdir', 'getcwd', 'listdir', 'mkdir', 'remove', 'rename', 'rmdir', 
           'system', 'environ'},

    # Módulo sys
    'sys': {'exit', 'argv', 'path', 'stdin', 'stdout', 'stderr', 'platform'},

    # Módulo datetime
    'datetime': {'datetime', 'date', 'time', 'timedelta', 'timezone', 'now', 'today', 'utcnow', 
                 'strftime', 'strptime'},

    # Módulo random
    'random': {'randint', 'uniform', 'choice', 'choices', 'sample', 'shuffle', 'seed'},

    # Módulo re (Expresiones Regulares)
    're': {'match', 'search', 'findall', 'sub', 'split', 'compile'},

    # Librería numpy
    'numpy': {'array', 'linspace', 'arange', 'zeros', 'ones', 'eye', 'dot', 'matmul', 'mean', 'median', 
              'std', 'var', 'min', 'max', 'sum', 'prod', 'shape', 'dtype', 'reshape', 'transpose', 
              'flatten', 'squeeze'},

    # Librería pandas
    'pandas': {'DataFrame', 'Series', 'read_csv', 'read_excel', 'to_csv', 'to_excel', 'loc', 'iloc', 
               'head', 'tail', 'merge', 'concat', 'groupby', 'pivot', 'apply', 'map', 'unique', 
               'value_counts', 'fillna', 'dropna', 'drop', 'rename'},

    # Librería matplotlib.pyplot
    'matplotlib.pyplot': {'plot', 'scatter', 'bar', 'hist', 'boxplot', 'xlabel', 'ylabel', 'title', 
                          'legend', 'grid', 'show', 'savefig'},

    # Librería sklearn
    'sklearn': {'fit', 'predict', 'transform', 'score', 'train_test_split', 'cross_val_score', 
                'accuracy_score', 'confusion_matrix', 'classification_report'},

    # Flask
    'flask': {'Flask', 'request', 'jsonify', 'render_template', 'session', 'redirect', 'url_for'},

    # Django
    'django': {'models', 'CharField', 'IntegerField', 'ForeignKey', 'ManyToManyField', 'views', 
               'forms', 'admin', 'urls', 'QuerySet', 'filter', 'get', 'all', 'save', 'delete'},

    # FastAPI
    'fastapi': {'FastAPI', 'APIRouter', 'HTTPException', 'Request', 'Response', 'Depends'},

    # SQL (usado en sqlite3, MySQL, etc.)
    'sql': {'SELECT', 'FROM', 'WHERE', 'JOIN', 'INNER', 'LEFT', 'RIGHT', 'FULL', 'GROUP', 'ORDER', 
            'LIMIT', 'OFFSET', 'INSERT', 'INTO', 'VALUES', 'UPDATE', 'SET', 'DELETE', 'CREATE', 
            'TABLE', 'DROP', 'ALTER', 'PRIMARY', 'FOREIGN', 'KEY', 'AUTO_INCREMENT', 'INDEX'},

    # MongoDB (pymongo)
    'pymongo': {'find', 'insert_one', 'insert_many', 'update_one', 'update_many', 'delete_one', 
                'delete_many', 'aggregate', 'sort', 'limit'},

    # asyncio
    'asyncio': {'async', 'await', 'create_task', 'run', 'sleep', 'gather', 'Event', 'Queue'},

    # Manejo de archivos (open)
    'file': {'read', 'readline', 'readlines', 'write', 'writelines', 'close', 'seek', 'tell', 'flush'},

    # JSON
    'json': {'load', 'loads', 'dump', 'dumps'},

    # XML
    'xml': {'parse', 'fromstring', 'find', 'findall', 'get', 'set', 'write'},

    # Requests (para peticiones HTTP)
    'requests': {'get', 'post', 'put', 'delete', 'json', 'headers', 'status_code', 'text'},

    # Sockets
    'socket': {'socket', 'bind', 'listen', 'accept', 'connect', 'send', 'recv', 'close'},
}
