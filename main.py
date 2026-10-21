def BeaconNodeSimulation (remainingDistance, timeA, timeB, historicalPeak, PWaiting, alpha =0.7):
  distanceAB = 500 #meters
  timeDiffAB = timeB - timeA #seconds
  speedAB = distanceAB / timeDiffAB #meter per second

  blendedSpeed = (alpha*speedAB) + (1 - alpha) * historicalPeak #meter per second if historical speed in meter per second
  travelTime = remainingDistance / blendedSpeed #second
  queueDelay = PWaiting * 3 #second
  totalETA = travelTime + queueDelay 
  finalSpeed_kmh = blendedSpeed * 3.6


  return round (totalETA / 60, 1), round (finalSpeed_kmh,1)

eta, speed = BeaconNodeSimulation (remainingDistance =500,
                                timeA = 0,
                                timeB = 55,
                                historicalPeak = 5.56,
                                PWaiting = 6,
                                alpha = 0.7)

print ("--- ADVANCED SIMULATION BEACONNODE ---")
print ("ETA (minutes) = " , eta)
print ("speed (km/h) = ", speed)
