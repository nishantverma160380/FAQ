from hcmintegration import retriever
import tempfile
import csv


def main():
    s3_retrieve = retriever.S3Retriever(f'mdev.peacock.people.extract.zeawpttbsz')
    new_file_path = s3_retrieve.find('HCM/CONSOLIDATED-DAILY-JML/b8d010cd-0415-4145-b9f7-b9659da21d22', '.*')
    #new_file_path = s3_retrieve.find('/INT_123/2019-03-26/ce69834c-1efc-43a8-a9db-95070f59372c/pending/original/', '.*/Consolidated_Daily_JML_Extract_\d{14}.txt')
    print(new_file_path)
    source = s3_retrieve.get_content(new_file_path)
    tmp = tempfile.TemporaryFile('w+')
    tmp.write(source)
    tmp.seek(0)
    source = tmp

    for row in csv.DictReader(source):
        print(row)


def open_s3_file(new_file_path, s3_retrieve):
    source = s3_retrieve.get_content(new_file_path)
    tmp = tempfile.TemporaryFile('w+')
    tmp.write(source)
    tmp.seek(0)
    return tmp


if __name__ == "__main__":
    main()
