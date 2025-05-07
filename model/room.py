class Room:
    __tablename__ = 'room'

    room_id = Column(Integer, primary_key=True)
    room_no = Column(String)
    price_per_night = Column(Float)

    room_type_id = Column(Integer, ForeignKey('room_type.room_type_id'))
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))

    room_type = relationship("RoomType", back_populates="rooms")
    facilities = relationship("Facilities", secondary=room_facilities, back_populates="rooms")
    bookings = relationship("Booking", back_populates="room")
