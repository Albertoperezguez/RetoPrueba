import sqlalchemy as db
import persistence.modelos as mod

engine = db.create_engine('sqlite:///db/login.sqlite', echo=True, future=True)
mod.Base.metadata.create_all(engine)
