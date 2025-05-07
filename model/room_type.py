class RoomType(Base):
    __tablename__ = 'room_type'

    room_type_id = Column(Integer, primary_key=True)
    description = Column(String)
    max_guests = Column(Integer)

    rooms = relationship("Room", back_populates="room_type")
