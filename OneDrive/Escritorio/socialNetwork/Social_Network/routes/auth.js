const router = require("express").Router();
const Lodging = require("../models/User");


//REGISTRO
router.post("/register", async (req, res) => {
  try {
    //crear nuevo hospedaje
    const newLodging = new Lodging({
      lodgingType: req.body.lodgingType,
      rooms: req.body.rooms,
      typeOfRoom: req.body.typeOfRoom,
      bathrooms: req.body.bathrooms,
      typeOfBathrooms: req.body.typeOfBathrooms,
      city: req.body.city,
      country: req.body.country,
      address: req.body.address,
      numOfGuests: req.body.numOfGuests,
      checkIn: req.body.CheckIn,
      checkOut:req.body.CheckOut,
    });
    // guardar  y respuesta
    const lodging = await newLodging.save();
    res.status(200).json(lodging);
  } catch (err) {
    res.json(err);
  }
});


module.exports = router;
