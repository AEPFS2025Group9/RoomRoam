Base = declarative_base()

class Booking(Base):
    __tablename__ = 'booking'

    booking_id = Column(Integer, primary_key=True)
    check_in_date = Column(Date)
    check_out_date = Column(Date)
    is_cancelled = Column(Boolean)
    total_amount = Column(Float)
    attribute = Column(String)

    guest_id = Column(Integer, ForeignKey('guest.guest_id'))
    room_id = Column(Integer, ForeignKey('room.room_id'))

    guest = relationship("Guest", back_populates="bookings")
