import os
from testing.utils.logs.logger import Logger


def get_logger_with_context(request):
    # Get the full path
    test_file = str(request.node.fspath)
    # Get the project root (adjust as needed)
    project_root = os.path.abspath(os.getcwd())
    # Make the path relative to the project root
    rel_path = os.path.relpath(test_file, project_root)
    test_name = request.node.name
    log_line_prefix = f"[{rel_path}::{test_name}]"
    logger_instance = Logger()
    logger_with_context = logger_instance.get_adapter(test_context=log_line_prefix)
    return logger_with_context
