from project.repository import session_repository
from project.use_cases.turn import Turn


class GameSession:
    """
    Create the object game session. A game session must have:
        - name
        - turns
        - players
    A game session may be:
        - started
        - finished
    """

    def __init__(self, name, players: list = [], turn: Turn = None, started=False, finished=False):
        self.name = name
        self.players = players
        self.turn = turn
        self.started = started
        self.finished = finished

    def __eq__(self, other):
        if isinstance(other, GameSession):
            return self.name == other.name and self.players == other.players \
                   and self.started == other.started and self.finished == other.finished
        return False

    @staticmethod
    def create_session(name):
        session = GameSession(name)
        session_repository.save(session)
        return session

    def add_players(self, name, players: list):
        session = self._find_session(name)
        session.players = players
        session_repository.update(session)
        return session

    def start(self, name):
        session = self._find_session(name)
        if not session.players:
            raise Exception
        session.started = True
        session_repository.update(session)
        return session

    def finish(self, name):
        session = self._find_session(name)
        if not session.started:
            raise Exception
        session.finished = True
        session_repository.update(session)
        return session

    @staticmethod
    def _find_session(name):
        return session_repository.find_session_by_name(name)