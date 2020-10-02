from _datetime import datetime
import csv


class LogRecord:
    def __init__(self, log_line: str):
        parts = log_line.split(maxsplit=7)
        self.timestamp = datetime.fromisoformat(parts[0] + ' ' + parts[1])
        self.log_level = parts[2]
        self.pid = parts[3]
        self.thread = parts[5][1:-1]
        self.logger = parts[6]
        self.message = parts[7][2:]


def convert_log_file_to_tsv(file_path: str, file_encoding: str):
    log_file = open(file_path, encoding=file_encoding)
    tsv_file = open(file_path.replace('.log', '.tsv'), 'w')
    writer = csv.writer(tsv_file, delimiter='\t', lineterminator="\n", escapechar='\\', quotechar='\"')
    write_headers(writer)
    for line in log_file.readlines():
        log_record = LogRecord(line.strip('\n'))
        append_log(writer, log_record)
    log_file.close()
    tsv_file.close()


def write_headers(writer):
    writer.writerow(['timestamp', 'log_level', 'pid', 'thread', 'logger', 'message'])


def append_log(writer, record: LogRecord):
    writer.writerow([record.timestamp.strftime('%Y-%m-%d %H:%M:%S.%f'),
                     record.log_level,
                     record.pid,
                     record.thread,
                     record.logger,
                     record.message])


test_file_path = 'E:\\Учёба\\РИС\\1 семестр\\Алг. языки программирования (Python)\\lab\\lab3\\resources\\sample.log'
test_file_encoding = 'utf-8'

if __name__ == "__main__":
    convert_log_file_to_tsv(test_file_path, test_file_encoding)

