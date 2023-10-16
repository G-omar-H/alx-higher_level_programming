#!/usr/bin/python3
"""Almost cycle Alx learnirng project"""
import json
import csv


class Base:
    """
    base class for the upcoming project...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        Base.__nb_objects += 1
        if id is None:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a json representation of list_disctionary
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save the json representation of a string
        args:
            @list-objs: list of object to serialize by json to a file
            @cls: class to represente
        """

        path = "{}.json".format(cls.__name__)
        with open(path, "w", encoding="UTF8") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                obj_list = [ins.to_dictionary() for ins in list_objs]
                fd.write(Base.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list rom the json representation
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creat a new instance with attributres value in dictinnary
        @args:
            cls: class type creat
            disctionary: key worded list eith attributes and values
        """
        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 3)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of all instances
        @args:
            cls: class to initiate instances from
        """
        path = "{}.json".format(cls.__name__)
        try:
            with open(path, "r", encoding="UTF8") as fd:
                obj_list = Base.from_json_string(fd.read())
                return [cls.create(**d) for d in obj_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        write class attributed into CSV format inside a csv file
        @args:
            cls: class to convert
            list_object: list of objcect attributes to convert into CVS format
        """
        path = "{}.csv".format(csv.__name__)
        with open(path, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ins in list_objs:
                    writer.writerow(ins.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        load from a csv file a deserialazed data from csv format
        @args:
            cls: class to initiate instances from
        """
        path = "{}.csv".format(csv.__name__)
        try:
            with open(path, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dict = [dict([k, int(v)] for k, v in d.items())
                             for d in list_dict]
                return (cls.create(**d) for d in list_dict)
        except IOError:
            return []
