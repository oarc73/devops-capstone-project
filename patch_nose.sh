#!/bin/bash
find .venv/lib/python3.10/site-packages/nose -name "*.py" -exec sed -i 's/collections\.Callable/collections.abc.Callable/g' {} \;
echo "Parche completado"
