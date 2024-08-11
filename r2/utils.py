import math
from os.path import splitext
from datetime import timezone

filetypes_map = {
  ".txt": "Text Document",
  ".doc": "Word Document",
  ".docx": "Word Document",
  ".pdf": "PDF Document",
  ".xls": "Excel Spreadsheet",
  ".xlsx": "Excel Spreadsheet",
  ".ppt": "PowerPoint Presentation",
  ".pptx": "PowerPoint Presentation",
  ".jpg": "Image (JPEG)",
  ".jpeg": "Image (JPEG)",
  ".png": "Image (PNG)",
  ".gif": "Image (GIF)",
  ".bmp": "Image (Bitmap)",
  ".tiff": "Image (TIFF)",
  ".raw": "Image (Raw)",
  ".psd": "Image (Adobe Photoshop)",
  ".ai": "Image (Adobe Illustrator)",
  ".svg": "Vector Image (SVG)",
  ".mp3": "Audio (MP3)",
  ".mp4": "Video (MP4)",
  ".avi": "Video (AVI)",
  ".html": "HTML File",
  ".htm": "HTML File",
  ".css": "CSS File",
  ".js": "JavaScript File",
  ".py": "Python Script",
  ".java": "Java Source Code",
  ".cpp": "C++ Source Code",
  ".zip": "Zipped Archive",
  ".rar": "RAR Archive",
  ".exe": "Executable File",
  ".dll": "Dynamic Link Library",
  ".apk": "Android Package",
  ".iso": "Disk Image",
  ".rtf": "Rich Text Document",
  ".odt": "Open Document Text",
  ".docm": "Word Macro-Enabled Document",
  ".dotx": "Word Template",
  ".odp": "Open Document Presentation",
  ".ods": "Open Document Spreadsheet",
  ".odg": "Open Document Graphics",
  ".odc": "Open Document Chart",
  ".odf": "Open Document Formula",
  ".csv": "CSV File",
  ".json": "JSON File"
}


def process_file(content, path):
    return {
        'filename': content.get('Key').replace(path, ''),
        'type': filetypes_map.get(splitext(content.get('Key'))[1], 'Unknown'),
        'size': content.get('Size'),
        'lastModified': content.get('LastModified').replace(tzinfo=timezone.utc).timestamp()
    }


def remove_prefix_from_path(content, key, path):
    content[key] = content.get(key).replace(path, '')
    return content


def convert_size(size_bytes):
    """
    Convert a size in bytes to a human-readable string format.

    Args:
        size_bytes (int): Size in bytes.

    Returns:
        str: Human-readable string format (e.g., "10MB", "38.5MB", "5GB").
    """
    if size_bytes == 0:
      return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)

    # Remove unnecessary decimals (e.g., 10.0MB -> 10MB)
    if s.is_integer():
      s = int(s)

    return f"{s}{size_name[i]}"


def convert_response(file: dict):
    file["size"] = convert_size(file["size"])
    return file
