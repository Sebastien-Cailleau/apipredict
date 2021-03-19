import logging

from fastapi.responses import JSONResponse

from app.custom_logging import CustomizeLogger


logger = logging.getLogger(__name__)
logger = CustomizeLogger.make_logger()


def exception_log_json(error_message):
    """
    log and return error_message
    """
    logger.error(
        f"Error: {error_message} -- ABBORT -- "
    )
    return JSONResponse(
        status_code=400,
        content={
            "ok": False,
            "detail": error_message.args
        }
    )


def is_register(cursor, login):
    '''
    check if the FQDN with this login is already registered
    '''

    query = "SELECT username, value FROM radcheck WHERE username = %s"
    cursor.execute(query, (login,))
    if cursor.fetchall():
        return True
    else:
        raise ValueError(f"Login: {login} is not register")


def is_not_register(cursor, login):
    '''
    check if the FQDN with this login is not registered
    '''

    query = "SELECT username, value FROM radcheck WHERE username = %s"
    cursor.execute(query, (login,))
    if cursor.fetchall():
        raise ValueError(f"Login: {login} is already registered")
    else:
        return True
