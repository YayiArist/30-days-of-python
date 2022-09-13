const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema 
({
  lodgingType: { type: String },

  rooms: { type: Number, default: null },
  typeOfRoom: [{ type: String, default: null }],
  bathrooms: { type: Number },
  typeOfBathrooms: { type: String },

  city: { type: String },
  country: { type: String },
  address: { type: String },
  numOfGuests: { type: Number },
  checkIn: { type: String },
  checkOut: { type: String },
  services: {
    wifi: { type: String },
    ac: { type: Boolean},
    tv: { type: Boolean },
    security: { type: Boolean },
    cleaning: { type: Boolean },
    parking: { type: Boolean },
    laundry: { type: Boolean },
    hotWater: { type: Boolean },
    kitchen: { type: Boolean },
    pool: { type: Boolean },
    dining: { type: Boolean },
    pets: { type: Boolean },
  },
  description: { type: String },
});

module.exports = mongoose.model("User", UserSchema);
