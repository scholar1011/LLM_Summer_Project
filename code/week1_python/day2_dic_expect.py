from pathlib import Path
path = Path("test.")
def scan_txt (folder_path):
    p = Path(folder_path)
    for file in p.glob("*.txt"):
        if file.is_file():
            print(f'文本文件的路径是{file}')
def safe_read_file (file_path):
    path=Path(file_path)
    try:
        with open(path, "r", encoding="utf-8") as p:
            content=p.read()
    except FileNotFoundError:
        print(f"错误：{p}文件不存在")
    except UnicodeDecodeError:
        print(f"错误：编码不是uft-8，读取失败")
    except PermissionError:
        print(f"错误：没错权限读取文件")
    except Exception as e:
        print(f"未知错误:{e}")
    else:
        return content
    finally:
        print(f"本次的文件读取工作执行完毕\n")
def test_seek (path_file):
    path=Path(path_file)
    with open(path,"w+",encoding="uft-8")as f:
        f.write("如果有一天我变的很有钱")
        f.seek(0)
        content=f.read()
        print(f"打印的内容:{content}")
def batch_read_txt_count_lines (folder):
    root = Path(folder)
    for file in root.glob("*.txt"):
        try:
            with open(file,'r',encoding="utf-8")as f:
                lines=f.readlines()
        except Exception as err:
            print(f'{file.name}读取失败，原因：{err}')
        else:
            print(f'{file.name}总行数:{len(lines)}')

