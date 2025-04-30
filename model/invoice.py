Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoice'

    invoice_id = Column(Integer, primary_key=True)
    date_issued = Column(Date)
    amount_due = Column(Float)
    is_paid = Column(Boolean)

    booking_id = Column(Integer, ForeignKey('booking.booking_id'))

    booking = relationship("Booking", back_populates="invoice")
