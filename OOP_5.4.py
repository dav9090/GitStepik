'''����� ReversibleString
���������� ����� ReversibleString, ����������� ������. ��� �������� ���������� ����� ������ ��������� ���� ��������:

string � �������� ������
��������� ������ ReversibleString ������ ����� ��������� ������������ ��������� �������������:

<�������� ������>
����� ��������� ������ ReversibleString ������ ������������ ������� �������� -, ����������� �������� ������ �������� ����� ��������� ������ ReversibleString �� ��������� ������ � �������� �������.

���������� 1. �������������� �������� ������ �� ������������ �� ���������. �������������, ��� ������������� ����� ������������ ������ � ����������� �������.

���������� 2. ������� ����������� ���������� ���������� ������ ReversibleString ���, ��� ����� ���� ������������.'''


class ReversibleString:
    def __init__(self, string: str):
        self.string = string

    def __str__(self):
        return self.string

    def __neg__(self):
        return ReversibleString(self.string[::-1])


string = ReversibleString('python')

print(string)
print(-string)