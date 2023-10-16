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
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
