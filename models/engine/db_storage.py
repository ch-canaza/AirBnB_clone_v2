#!/usr/bin/python3
""" defines class DBStorage """

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData, create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """ defines database called DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ initialization of  DBStorage """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        DBStorage.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                           .format(user, password, host, db),
                                           pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    """
    def all(self, cls=None):
        Returns a dictionary of models currently in db_storage
        new_dict = {}
        if cls is None:
            new_query = DBStorage.__session.query(User, State, City,
                                                  Amenity, Place, Review).all()
            for obj in new_query:
                new_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
            return new_dict
        else:
            new_query = DBStorage.__session.query(cls).all()
            for obj in new_query:
                new_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
            return new_dict
    """
    def all(self, cls=None):
        """must return a dictionary: (like FileStorage)
            all elements in database"""
        if not self.__session:
            self.reload()
        database_dic = {}
        if cls is not None:
            objects = DBStorage.__session.query(cls).all()
            for objs in objects:
                key = "{}.{}".format(type(objs).__class__.__name__, objs.id)
                database_dic[key] = objs
            return database_dic
        else:
            for objs in DBStorage.__session.query(City, State, User,
                                                  Place, Review,
                                                  Amenity).all():
                key = "{}.{}".format(type(objs).__class__.__name__, objs.id)
                database_dic[key] = objs
            return database_dic

    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ * create all tables in the database (feature\
             of SQLAlchemy) (WARNING: all classes who \
             inherit from Base must be imported before \
             calling Base.metadata.create_all(engine))
            * create the current database session\
             (self.__session) from the engine\
            (self.__engine) by using a \
            sessionmaker - the option expire_on_commit \
            must be set to False ; and scoped_session - \
                to make sure your Session is thread-safe"""

        Base.metadata.create_all(DBStorage.__engine)
        session = sessionmaker(bind=DBStorage.__engine,
                               expire_on_commit=False)
        Session = scoped_session(session)
        DBStorage.__session = Session()

    def close(self):
        '''
            Closes the current __session attribute
        '''
        self.__session.close()
