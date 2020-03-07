from cryptography.fernet import Fernet
import imports.fileReader as reader
import imports.CONSTS as CONSTS
import imports.dataHandler as jdata


jd = jdata.dataBase("tt");
jd.save();