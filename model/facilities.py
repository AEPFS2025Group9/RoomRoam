class Facilities(Base):
    __tablename__ = 'facilities'

    facility_id = Column(Integer, primary_key=True)
    facility_name = Column(String)

    rooms = relationship("Room", secondary=room_facilities, back_populates="facilities")
