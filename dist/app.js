// GEC Raipur 1990-91 Living Yearbook Application

// Complete roster data embedded to guarantee zero CORS issues when opened directly via file://
const ROSTER_DATA = [
  {
    "id": "sit-01",
    "name": "Dr. Y. P. Jain",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 1,
    "x": 90,
    "y": 604,
    "r": 22,
    "category": "sitting",
    "pct_x": 7.5,
    "pct_y": 67.713,
    "pct_r": 1.833
  },
  {
    "id": "sit-02",
    "name": "Prof. M. M. Tiwari",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 2,
    "x": 181,
    "y": 612,
    "r": 22,
    "category": "sitting",
    "pct_x": 15.083,
    "pct_y": 68.61,
    "pct_r": 1.833
  },
  {
    "id": "sit-03",
    "name": "Shri D. K. Tripathi",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 3,
    "x": 258,
    "y": 615,
    "r": 22,
    "category": "sitting",
    "pct_x": 21.5,
    "pct_y": 68.946,
    "pct_r": 1.833
  },
  {
    "id": "sit-04",
    "name": "Shri Anil Shastri",
    "role": "L & T Member",
    "row": "Sitting (Front Row)",
    "pos": 4,
    "x": 332,
    "y": 615,
    "r": 22,
    "category": "sitting",
    "pct_x": 27.667,
    "pct_y": 68.946,
    "pct_r": 1.833
  },
  {
    "id": "sit-05",
    "name": "Shri M. M. Rao",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 5,
    "x": 405,
    "y": 615,
    "r": 22,
    "category": "sitting",
    "pct_x": 33.75,
    "pct_y": 68.946,
    "pct_r": 1.833
  },
  {
    "id": "sit-06",
    "name": "Shri V. G. Deshpande",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 6,
    "x": 472,
    "y": 615,
    "r": 22,
    "category": "sitting",
    "pct_x": 39.333,
    "pct_y": 68.946,
    "pct_r": 1.833
  },
  {
    "id": "sit-07",
    "name": "Shri S. K. Tiwari",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 7,
    "x": 532,
    "y": 620,
    "r": 22,
    "category": "sitting",
    "pct_x": 44.333,
    "pct_y": 69.507,
    "pct_r": 1.833
  },
  {
    "id": "sit-08",
    "name": "Dr. H. A. Vachhani",
    "role": "Principal",
    "row": "Sitting (Front Row)",
    "pos": 8,
    "x": 600,
    "y": 618,
    "r": 24,
    "category": "sitting",
    "pct_x": 50.0,
    "pct_y": 69.283,
    "pct_r": 2.0
  },
  {
    "id": "sit-09",
    "name": "Prof. G. S. Verma",
    "role": "H. O. D. Mech",
    "row": "Sitting (Front Row)",
    "pos": 9,
    "x": 674,
    "y": 618,
    "r": 23,
    "category": "sitting",
    "pct_x": 56.167,
    "pct_y": 69.283,
    "pct_r": 1.917
  },
  {
    "id": "sit-10",
    "name": "Dr. M. L. Jeswani",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 10,
    "x": 741,
    "y": 616,
    "r": 22,
    "category": "sitting",
    "pct_x": 61.75,
    "pct_y": 69.058,
    "pct_r": 1.833
  },
  {
    "id": "sit-11",
    "name": "Dr. D. K. Mishra",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 11,
    "x": 816,
    "y": 615,
    "r": 22,
    "category": "sitting",
    "pct_x": 68.0,
    "pct_y": 68.946,
    "pct_r": 1.833
  },
  {
    "id": "sit-12",
    "name": "Dr. R. P. Sukhija",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 12,
    "x": 883,
    "y": 615,
    "r": 22,
    "category": "sitting",
    "pct_x": 73.583,
    "pct_y": 68.946,
    "pct_r": 1.833
  },
  {
    "id": "sit-13",
    "name": "Dr. Y. K. Gour",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 13,
    "x": 960,
    "y": 612,
    "r": 22,
    "category": "sitting",
    "pct_x": 80.0,
    "pct_y": 68.61,
    "pct_r": 1.833
  },
  {
    "id": "sit-14",
    "name": "Dr. D. G. Motwani",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 14,
    "x": 1033,
    "y": 615,
    "r": 22,
    "category": "sitting",
    "pct_x": 86.083,
    "pct_y": 68.946,
    "pct_r": 1.833
  },
  {
    "id": "sit-15",
    "name": "Miss. S. L. Sinha",
    "role": "Faculty",
    "row": "Sitting (Front Row)",
    "pos": 15,
    "x": 1103,
    "y": 626,
    "r": 22,
    "category": "sitting",
    "pct_x": 91.917,
    "pct_y": 70.179,
    "pct_r": 1.833
  },
  {
    "id": "std1-01",
    "name": "Nishtha Kothuria",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 1,
    "x": 86,
    "y": 550,
    "r": 19,
    "category": "standing1",
    "pct_x": 7.167,
    "pct_y": 61.659,
    "pct_r": 1.583
  },
  {
    "id": "std1-02",
    "name": "Prachee Sthapak",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 2,
    "x": 165,
    "y": 540,
    "r": 19,
    "category": "standing1",
    "pct_x": 13.75,
    "pct_y": 60.538,
    "pct_r": 1.583
  },
  {
    "id": "std1-03",
    "name": "A. K. Shukla",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 3,
    "x": 235,
    "y": 535,
    "r": 18,
    "category": "standing1",
    "pct_x": 19.583,
    "pct_y": 59.978,
    "pct_r": 1.5
  },
  {
    "id": "std1-04",
    "name": "Shailesh Tiwari",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 4,
    "x": 301,
    "y": 528,
    "r": 18,
    "category": "standing1",
    "pct_x": 25.083,
    "pct_y": 59.193,
    "pct_r": 1.5
  },
  {
    "id": "std1-05",
    "name": "R. K. Agrawal",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 5,
    "x": 355,
    "y": 545,
    "r": 18,
    "category": "standing1",
    "pct_x": 29.583,
    "pct_y": 61.099,
    "pct_r": 1.5
  },
  {
    "id": "std1-06",
    "name": "Sanjoy Halder",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 6,
    "x": 418,
    "y": 540,
    "r": 18,
    "category": "standing1",
    "pct_x": 34.833,
    "pct_y": 60.538,
    "pct_r": 1.5
  },
  {
    "id": "std1-07",
    "name": "Pravin Bakshi",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 7,
    "x": 479,
    "y": 545,
    "r": 18,
    "category": "standing1",
    "pct_x": 39.917,
    "pct_y": 61.099,
    "pct_r": 1.5
  },
  {
    "id": "std1-08",
    "name": "Ashok",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 8,
    "x": 538,
    "y": 538,
    "r": 18,
    "category": "standing1",
    "pct_x": 44.833,
    "pct_y": 60.314,
    "pct_r": 1.5
  },
  {
    "id": "std1-09",
    "name": "A. R. Sharif",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 9,
    "x": 591,
    "y": 540,
    "r": 18,
    "category": "standing1",
    "pct_x": 49.25,
    "pct_y": 60.538,
    "pct_r": 1.5
  },
  {
    "id": "std1-10",
    "name": "R. L. Kurrey",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 10,
    "x": 653,
    "y": 542,
    "r": 18,
    "category": "standing1",
    "pct_x": 54.417,
    "pct_y": 60.762,
    "pct_r": 1.5
  },
  {
    "id": "std1-11",
    "name": "I. C. Bharti",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 11,
    "x": 716,
    "y": 542,
    "r": 18,
    "category": "standing1",
    "pct_x": 59.667,
    "pct_y": 60.762,
    "pct_r": 1.5
  },
  {
    "id": "std1-12",
    "name": "Paresh Gohil",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 12,
    "x": 787,
    "y": 536,
    "r": 18,
    "category": "standing1",
    "pct_x": 65.583,
    "pct_y": 60.09,
    "pct_r": 1.5
  },
  {
    "id": "std1-13",
    "name": "A. A. Varwandkar",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 13,
    "x": 858,
    "y": 535,
    "r": 18,
    "category": "standing1",
    "pct_x": 71.5,
    "pct_y": 59.978,
    "pct_r": 1.5
  },
  {
    "id": "std1-14",
    "name": "V. Bhaskar Sharma",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 14,
    "x": 925,
    "y": 550,
    "r": 18,
    "category": "standing1",
    "pct_x": 77.083,
    "pct_y": 61.659,
    "pct_r": 1.5
  },
  {
    "id": "std1-15",
    "name": "A. P. Singh",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 15,
    "x": 992,
    "y": 548,
    "r": 18,
    "category": "standing1",
    "pct_x": 82.667,
    "pct_y": 61.435,
    "pct_r": 1.5
  },
  {
    "id": "std1-16",
    "name": "Sanjay Gupta",
    "role": "Student",
    "row": "Standing (1st Row)",
    "pos": 16,
    "x": 1076,
    "y": 545,
    "r": 19,
    "category": "standing1",
    "pct_x": 89.667,
    "pct_y": 61.099,
    "pct_r": 1.583
  },
  {
    "id": "std2-01",
    "name": "K. V. Raman Rao",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 1,
    "x": 116,
    "y": 468,
    "r": 17,
    "category": "standing2",
    "pct_x": 9.667,
    "pct_y": 52.466,
    "pct_r": 1.417
  },
  {
    "id": "std2-02",
    "name": "S. K. Agrawal",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 2,
    "x": 165,
    "y": 468,
    "r": 17,
    "category": "standing2",
    "pct_x": 13.75,
    "pct_y": 52.466,
    "pct_r": 1.417
  },
  {
    "id": "std2-03",
    "name": "Ravindra Dharkar",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 3,
    "x": 230,
    "y": 472,
    "r": 17,
    "category": "standing2",
    "pct_x": 19.167,
    "pct_y": 52.915,
    "pct_r": 1.417
  },
  {
    "id": "std2-04",
    "name": "K. K. Jha",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 4,
    "x": 282,
    "y": 472,
    "r": 17,
    "category": "standing2",
    "pct_x": 23.5,
    "pct_y": 52.915,
    "pct_r": 1.417
  },
  {
    "id": "std2-05",
    "name": "B. Raghu Kaushik",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 5,
    "x": 341,
    "y": 468,
    "r": 17,
    "category": "standing2",
    "pct_x": 28.417,
    "pct_y": 52.466,
    "pct_r": 1.417
  },
  {
    "id": "std2-06",
    "name": "Piyush Choudhary",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 6,
    "x": 396,
    "y": 468,
    "r": 17,
    "category": "standing2",
    "pct_x": 33.0,
    "pct_y": 52.466,
    "pct_r": 1.417
  },
  {
    "id": "std2-07",
    "name": "S. K. Dwivedi",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 7,
    "x": 454,
    "y": 468,
    "r": 17,
    "category": "standing2",
    "pct_x": 37.833,
    "pct_y": 52.466,
    "pct_r": 1.417
  },
  {
    "id": "std2-08",
    "name": "Maya Ram",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 8,
    "x": 508,
    "y": 470,
    "r": 17,
    "category": "standing2",
    "pct_x": 42.333,
    "pct_y": 52.691,
    "pct_r": 1.417
  },
  {
    "id": "std2-09",
    "name": "Jitendra Motwani",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 9,
    "x": 562,
    "y": 468,
    "r": 17,
    "category": "standing2",
    "pct_x": 46.833,
    "pct_y": 52.466,
    "pct_r": 1.417
  },
  {
    "id": "std2-10",
    "name": "R. K. Shrivastava",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 10,
    "x": 611,
    "y": 474,
    "r": 17,
    "category": "standing2",
    "pct_x": 50.917,
    "pct_y": 53.139,
    "pct_r": 1.417
  },
  {
    "id": "std2-11",
    "name": "M. H. Soni",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 11,
    "x": 666,
    "y": 472,
    "r": 17,
    "category": "standing2",
    "pct_x": 55.5,
    "pct_y": 52.915,
    "pct_r": 1.417
  },
  {
    "id": "std2-12",
    "name": "Sandeep Jain",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 12,
    "x": 720,
    "y": 472,
    "r": 17,
    "category": "standing2",
    "pct_x": 60.0,
    "pct_y": 52.915,
    "pct_r": 1.417
  },
  {
    "id": "std2-13",
    "name": "K. K. Thakur",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 13,
    "x": 776,
    "y": 472,
    "r": 17,
    "category": "standing2",
    "pct_x": 64.667,
    "pct_y": 52.915,
    "pct_r": 1.417
  },
  {
    "id": "std2-14",
    "name": "Deepak Rao",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 14,
    "x": 831,
    "y": 475,
    "r": 17,
    "category": "standing2",
    "pct_x": 69.25,
    "pct_y": 53.251,
    "pct_r": 1.417
  },
  {
    "id": "std2-15",
    "name": "Sheikh Zakir",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 15,
    "x": 887,
    "y": 474,
    "r": 17,
    "category": "standing2",
    "pct_x": 73.917,
    "pct_y": 53.139,
    "pct_r": 1.417
  },
  {
    "id": "std2-16",
    "name": "Anirban Dutta",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 16,
    "x": 941,
    "y": 475,
    "r": 17,
    "category": "standing2",
    "pct_x": 78.417,
    "pct_y": 53.251,
    "pct_r": 1.417
  },
  {
    "id": "std2-17",
    "name": "Abhay Agrawal",
    "role": "Student",
    "row": "Standing (2nd Row)",
    "pos": 17,
    "x": 1017,
    "y": 475,
    "r": 17,
    "category": "standing2",
    "pct_x": 84.75,
    "pct_y": 53.251,
    "pct_r": 1.417
  },
  {
    "id": "std3-01",
    "name": "Vinay Awasthi",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 1,
    "x": 138,
    "y": 432,
    "r": 16,
    "category": "standing3",
    "pct_x": 11.5,
    "pct_y": 48.43,
    "pct_r": 1.333
  },
  {
    "id": "std3-02",
    "name": "Kajal Roy",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 2,
    "x": 211,
    "y": 405,
    "r": 16,
    "category": "standing3",
    "pct_x": 17.583,
    "pct_y": 45.404,
    "pct_r": 1.333
  },
  {
    "id": "std3-03",
    "name": "Makrand Mahajan",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 3,
    "x": 263,
    "y": 400,
    "r": 16,
    "category": "standing3",
    "pct_x": 21.917,
    "pct_y": 44.843,
    "pct_r": 1.333
  },
  {
    "id": "std3-04",
    "name": "Piyush Banafar",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 4,
    "x": 309,
    "y": 400,
    "r": 16,
    "category": "standing3",
    "pct_x": 25.75,
    "pct_y": 44.843,
    "pct_r": 1.333
  },
  {
    "id": "std3-05",
    "name": "Sandeep Kulkarni",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 5,
    "x": 359,
    "y": 408,
    "r": 16,
    "category": "standing3",
    "pct_x": 29.917,
    "pct_y": 45.74,
    "pct_r": 1.333
  },
  {
    "id": "std3-06",
    "name": "Hemant Jethi",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 6,
    "x": 408,
    "y": 405,
    "r": 16,
    "category": "standing3",
    "pct_x": 34.0,
    "pct_y": 45.404,
    "pct_r": 1.333
  },
  {
    "id": "std3-07",
    "name": "Hakimuddin Ali",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 7,
    "x": 461,
    "y": 405,
    "r": 16,
    "category": "standing3",
    "pct_x": 38.417,
    "pct_y": 45.404,
    "pct_r": 1.333
  },
  {
    "id": "std3-08",
    "name": "D. Shakhare",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 8,
    "x": 516,
    "y": 410,
    "r": 16,
    "category": "standing3",
    "pct_x": 43.0,
    "pct_y": 45.964,
    "pct_r": 1.333
  },
  {
    "id": "std3-09",
    "name": "S. K. Khote",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 9,
    "x": 568,
    "y": 408,
    "r": 16,
    "category": "standing3",
    "pct_x": 47.333,
    "pct_y": 45.74,
    "pct_r": 1.333
  },
  {
    "id": "std3-10",
    "name": "Sanjay Nagpure",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 10,
    "x": 624,
    "y": 410,
    "r": 16,
    "category": "standing3",
    "pct_x": 52.0,
    "pct_y": 45.964,
    "pct_r": 1.333
  },
  {
    "id": "std3-11",
    "name": "B. D. Markande",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 11,
    "x": 651,
    "y": 415,
    "r": 16,
    "category": "standing3",
    "pct_x": 54.25,
    "pct_y": 46.525,
    "pct_r": 1.333
  },
  {
    "id": "std3-12",
    "name": "P. K. Banjare",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 12,
    "x": 678,
    "y": 425,
    "r": 16,
    "category": "standing3",
    "pct_x": 56.5,
    "pct_y": 47.646,
    "pct_r": 1.333
  },
  {
    "id": "std3-13",
    "name": "V. K. Khaiklo",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 13,
    "x": 705,
    "y": 422,
    "r": 16,
    "category": "standing3",
    "pct_x": 58.75,
    "pct_y": 47.309,
    "pct_r": 1.333
  },
  {
    "id": "std3-14",
    "name": "R. S. Chhatra",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 14,
    "x": 765,
    "y": 420,
    "r": 16,
    "category": "standing3",
    "pct_x": 63.75,
    "pct_y": 47.085,
    "pct_r": 1.333
  },
  {
    "id": "std3-15",
    "name": "Manish Mishra",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 15,
    "x": 817,
    "y": 410,
    "r": 16,
    "category": "standing3",
    "pct_x": 68.083,
    "pct_y": 45.964,
    "pct_r": 1.333
  },
  {
    "id": "std3-16",
    "name": "Yuvraj Kashley",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 16,
    "x": 865,
    "y": 412,
    "r": 16,
    "category": "standing3",
    "pct_x": 72.083,
    "pct_y": 46.188,
    "pct_r": 1.333
  },
  {
    "id": "std3-17",
    "name": "M. K. Dhruwe",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 17,
    "x": 915,
    "y": 415,
    "r": 16,
    "category": "standing3",
    "pct_x": 76.25,
    "pct_y": 46.525,
    "pct_r": 1.333
  },
  {
    "id": "std3-18",
    "name": "C. S. Bhagat",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 18,
    "x": 965,
    "y": 422,
    "r": 16,
    "category": "standing3",
    "pct_x": 80.417,
    "pct_y": 47.309,
    "pct_r": 1.333
  },
  {
    "id": "std3-19",
    "name": "Mohan Singh",
    "role": "Student",
    "row": "Standing (3rd Row)",
    "pos": 19,
    "x": 1013,
    "y": 418,
    "r": 16,
    "category": "standing3",
    "pct_x": 84.417,
    "pct_y": 46.861,
    "pct_r": 1.333
  }
];

class LivingYearbookApp {
  constructor() {
    this.roster = ROSTER_DATA;
    this.filteredRoster = [...this.roster];
    this.activeFilter = "all";
    this.searchQuery = "";
    this.selectedPerson = null;

    // Viewport & Pan/Zoom State
    this.scale = 1.0;
    this.panX = 0;
    this.panY = 0;
    this.isDragging = false;
    this.startX = 0;
    this.startY = 0;

    // Calibration Mode State
    this.calibrationMode = false;
    this.calibratingPerson = null;

    // Local Storage for alumni profile updates
    this.profileUpdates = this.loadLocalUpdates();

    this.initDOMElements();
    this.initEventListeners();
    this.initAmbientReels();
    this.renderHotspots();
    this.renderRoster();
  }

  loadLocalUpdates() {
    try {
      const saved = localStorage.getItem("gec_raipur_1991_profiles");
      return saved ? JSON.parse(saved) : {};
    } catch (e) {
      return {};
    }
  }

  saveLocalUpdates() {
    try {
      localStorage.setItem("gec_raipur_1991_profiles", JSON.stringify(this.profileUpdates));
    } catch (e) {
      console.error("Local storage error:", e);
    }
  }

  initDOMElements() {
    this.viewport = document.getElementById("viewport");
    this.canvas = document.getElementById("canvas");
    this.mainPhoto = document.getElementById("mainPhoto");
    this.hotspotsLayer = document.getElementById("hotspotsLayer");
    this.searchInput = document.getElementById("searchInput");
    this.filterTabs = document.getElementById("filterTabs");
    this.alumniGrid = document.getElementById("alumniGrid");
    this.rosterCountBadge = document.getElementById("rosterCountBadge");
    this.selectedSummary = document.getElementById("selectedSummary");

    // Modal elements
    this.modalOverlay = document.getElementById("profileModalOverlay");
    this.closeModalBtn = document.getElementById("closeModalBtn");
    this.modalName = document.getElementById("modalName");
    this.modalRowRole = document.getElementById("modalRowRole");
    this.modalAvatar1991 = document.getElementById("modalAvatar1991");
    this.modalAvatarCurrent = document.getElementById("modalAvatarCurrent");
    this.uploadPlaceholder = document.getElementById("uploadPlaceholder");
    this.currentPhotoInput = document.getElementById("currentPhotoInput");
    this.profileCity = document.getElementById("profileCity");
    this.profileRole = document.getElementById("profileRole");
    this.profileContact = document.getElementById("profileContact");
    this.profileNickname = document.getElementById("profileNickname");
    this.profileMemory = document.getElementById("profileMemory");
    this.saveProfileBtn = document.getElementById("saveProfileBtn");
    this.modalSpotlightBtn = document.getElementById("modalSpotlightBtn");

    // View buttons
    this.viewDeskewedBtn = document.getElementById("viewDeskewedBtn");
    this.viewEnhancedBtn = document.getElementById("viewEnhancedBtn");
    this.viewOriginalBtn = document.getElementById("viewOriginalBtn");
    this.exportDataBtn = document.getElementById("exportDataBtn");

    // Theme Style Elements
    this.themeFrameContainer = document.getElementById("themeFrameContainer");
    this.themeFrameOverlay = document.getElementById("themeFrameOverlay");
    this.themeBtnGroup = document.getElementById("themeBtnGroup");
    this.downloadShareCardBtn = document.getElementById("downloadShareCardBtn");
    this.activeTheme = "none";

    // HUD buttons
    this.toggleReelsBtn = document.getElementById("toggleReelsBtn");
    this.toggleNamesBtn = document.getElementById("toggleNamesBtn");
    this.showAllNames = false;
    this.zoomInBtn = document.getElementById("zoomInBtn");
    this.zoomOutBtn = document.getElementById("zoomOutBtn");
    this.zoomResetBtn = document.getElementById("zoomResetBtn");
    this.calibrateBtn = document.getElementById("calibrateBtn");

    // Ambient Reels Elements
    this.stageMainArea = document.getElementById("stageMainArea");
    this.ambientReelLeft = document.getElementById("ambientReelLeft");
    this.ambientReelRight = document.getElementById("ambientReelRight");
    this.reelTrackLeft = document.getElementById("reelTrackLeft");
    this.reelTrackRight = document.getElementById("reelTrackRight");
    this.reelsVisible = localStorage.getItem("gec_reels_visible") !== "false";

    // Milestone Modal
    this.milestoneModalOverlay = document.getElementById("milestoneModalOverlay");
    this.closeMilestoneModalBtn = document.getElementById("closeMilestoneModalBtn");
    this.milestoneEraTag = document.getElementById("milestoneEraTag");
    this.milestoneModalTitle = document.getElementById("milestoneModalTitle");
    this.milestoneModalCategory = document.getElementById("milestoneModalCategory");
    this.milestoneModalSvg = document.getElementById("milestoneModalSvg");
    this.milestoneModalFormula = document.getElementById("milestoneModalFormula");
    this.milestoneModalDesc = document.getElementById("milestoneModalDesc");
    this.milestoneModalMemory = document.getElementById("milestoneModalMemory");

    // Toast
    this.toastMsg = document.getElementById("toastMsg");
  }

  initEventListeners() {
    // Zoom & Pan
    this.viewport.addEventListener("mousedown", (e) => this.onMouseDown(e));
    window.addEventListener("mousemove", (e) => this.onMouseMove(e));
    window.addEventListener("mouseup", () => this.onMouseUp());
    this.viewport.addEventListener("wheel", (e) => this.onWheel(e), { passive: false });

    // Touch support for mobile devices
    this.viewport.addEventListener("touchstart", (e) => this.onTouchStart(e), { passive: false });
    this.viewport.addEventListener("touchmove", (e) => this.onTouchMove(e), { passive: false });
    this.viewport.addEventListener("touchend", () => this.isDragging = false);

    // Zoom & Name Display Buttons
    if (this.toggleNamesBtn) {
      this.toggleNamesBtn.addEventListener("click", () => {
        this.showAllNames = !this.showAllNames;
        this.canvas.classList.toggle("show-all-names", this.showAllNames);
        this.toggleNamesBtn.classList.toggle("active", this.showAllNames);
        this.showToast(this.showAllNames ? "Showing all 67 names over the photo" : "Names hidden (hover face to view)");
      });
    }
    this.zoomInBtn.addEventListener("click", () => this.adjustZoom(0.25));
    this.zoomOutBtn.addEventListener("click", () => this.adjustZoom(-0.25));
    this.zoomResetBtn.addEventListener("click", () => this.resetZoom());

    // Search input
    this.searchInput.addEventListener("input", (e) => {
      this.searchQuery = e.target.value.toLowerCase().trim();
      this.filterAndRender();
    });

    // Filter tabs
    this.filterTabs.addEventListener("click", (e) => {
      const tab = e.target.closest(".filter-tab");
      if (!tab) return;
      this.filterTabs.querySelectorAll(".filter-tab").forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      this.activeFilter = tab.dataset.filter;
      this.filterAndRender();
    });

    // View Image Switchers
    this.viewDeskewedBtn.addEventListener("click", () => this.switchImageView("deskewed"));
    this.viewEnhancedBtn.addEventListener("click", () => this.switchImageView("enhanced"));
    this.viewOriginalBtn.addEventListener("click", () => this.switchImageView("original"));

    // Modal Events
    this.closeModalBtn.addEventListener("click", () => this.closeModal());
    this.modalOverlay.addEventListener("click", (e) => {
      if (e.target === this.modalOverlay) this.closeModal();
    });
    this.saveProfileBtn.addEventListener("click", () => this.saveCurrentProfile());
    this.modalSpotlightBtn.addEventListener("click", () => {
      if (this.selectedPerson) {
        this.closeModal();
        this.spotlightPerson(this.selectedPerson.id);
      }
    });

    // Photo Upload (Then & Now)
    this.currentPhotoInput.addEventListener("change", (e) => this.handleCurrentPhotoUpload(e));

    // Export updates
    this.exportDataBtn.addEventListener("click", () => this.exportUpdatesJSON());

    // 35th Jubilee Style Theme Switcher
    if (this.themeBtnGroup) {
      this.themeBtnGroup.addEventListener("click", (e) => {
        const btn = e.target.closest(".theme-pill");
        if (!btn) return;
        this.setTheme(btn.dataset.theme);
      });
    }

    if (this.downloadShareCardBtn) {
      this.downloadShareCardBtn.addEventListener("click", () => this.downloadShareCard());
    }

    // Calibration tool
    this.calibrateBtn.addEventListener("click", () => this.toggleCalibrationMode());
    document.getElementById("closeCalibrateBtn")?.addEventListener("click", () => this.toggleCalibrationMode(false));
    document.getElementById("copyJsonBtn")?.addEventListener("click", () => this.copyCoordinatesJSON());
  }

  /* Pan & Zoom Handlers */
  onMouseDown(e) {
    if (e.target.closest(".face-pin") && !this.calibrationMode) return;
    this.isDragging = true;
    this.startX = e.clientX - this.panX;
    this.startY = e.clientY - this.panY;
    this.viewport.classList.add("grabbing");
  }

  onMouseMove(e) {
    if (!this.isDragging) return;
    this.panX = e.clientX - this.startX;
    this.panY = e.clientY - this.startY;
    this.updateTransform();
  }

  onMouseUp() {
    this.isDragging = false;
    this.viewport.classList.remove("grabbing");
  }

  onWheel(e) {
    e.preventDefault();
    const zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
    this.adjustZoom(zoomFactor - 1, e.clientX, e.clientY);
  }

  onTouchStart(e) {
    if (e.touches.length === 1) {
      const t = e.touches[0];
      this.isDragging = true;
      this.startX = t.clientX - this.panX;
      this.startY = t.clientY - this.panY;
    }
  }

  onTouchMove(e) {
    if (!this.isDragging || e.touches.length !== 1) return;
    e.preventDefault();
    const t = e.touches[0];
    this.panX = t.clientX - this.startX;
    this.panY = t.clientY - this.startY;
    this.updateTransform();
  }

  adjustZoom(delta, clientX = null, clientY = null) {
    const oldScale = this.scale;
    this.scale = Math.max(0.8, Math.min(4.5, this.scale + delta));
    this.updateTransform();
  }

  resetZoom() {
    this.scale = 1.0;
    this.panX = 0;
    this.panY = 0;
    this.updateTransform();
  }

  updateTransform() {
    this.canvas.style.transform = `translate(${this.panX}px, ${this.panY}px) scale(${this.scale})`;
  }

  /* Image Switcher */
  switchImageView(type) {
    [this.viewDeskewedBtn, this.viewEnhancedBtn, this.viewOriginalBtn].forEach(b => b.classList.remove("active"));
    
    if (type === "deskewed") {
      this.mainPhoto.src = "assets/photo_deskewed.jpg";
      this.viewDeskewedBtn.classList.add("active");
      this.hotspotsLayer.style.display = "block";
    } else if (type === "enhanced") {
      this.mainPhoto.src = "assets/photo_enhanced.jpg";
      this.viewEnhancedBtn.classList.add("active");
      this.hotspotsLayer.style.display = "block";
    } else if (type === "original") {
      this.mainPhoto.src = "assets/photo_original.jpg";
      this.viewOriginalBtn.classList.add("active");
      this.hotspotsLayer.style.display = "none"; // Pins are calibrated to deskewed crop
      this.showToast("Showing original physical cardboard mount scan");
    }
  }

  /* 35th Jubilee Style Theme Switcher */
  setTheme(themeId) {
    this.activeTheme = themeId;
    if (this.themeBtnGroup) {
      this.themeBtnGroup.querySelectorAll(".theme-pill").forEach(p => {
        p.classList.toggle("active", p.dataset.theme === themeId);
      });
    }

    const themeTitles = {
      none: "Original Photo",
      archival: "Archival Silver-Gelatin",
      blueprint: "Mechanical Blueprint",
      contactsheet: "1991 35mm Contact Sheet",
      cinema: "1991 Retro Bollywood Card",
      cad: "AutoCAD R11 Slate"
    };

    if (themeId === "none") {
      if (this.themeFrameContainer) this.themeFrameContainer.classList.remove("themed");
      if (this.themeFrameOverlay) {
        this.themeFrameOverlay.style.display = "none";
        this.themeFrameOverlay.src = "";
      }
      this.showToast("Showing original photo view");
    } else {
      if (this.themeFrameContainer) this.themeFrameContainer.classList.add("themed");
      if (this.themeFrameOverlay) {
        this.themeFrameOverlay.src = `assets/themes/theme_${themeId}.svg`;
        this.themeFrameOverlay.style.display = "block";
      }
      this.showToast(`Switched style: ${themeTitles[themeId] || themeId}`);
    }
  }

  downloadShareCard() {
    const filename = this.activeTheme === "none"
      ? "assets/photo_deskewed.jpg"
      : `assets/themes/composite_${this.activeTheme}.jpg`;
    
    const downloadName = this.activeTheme === "none"
      ? "GEC_Raipur_1991_Mechanical_Original.jpg"
      : `GEC_Raipur_1991_${this.activeTheme}_WhatsApp_Card.jpg`;

    const a = document.createElement("a");
    a.href = filename;
    a.download = downloadName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    this.showToast("Exported WhatsApp share card!");
  }

  /* Render Interactive Hotspot Pins */
  renderHotspots() {
    this.hotspotsLayer.innerHTML = "";

    this.roster.forEach(person => {
      const pin = document.createElement("div");
      pin.className = "face-pin";
      pin.id = `pin-${person.id}`;
      pin.dataset.id = person.id;

      // Position using percentage
      pin.style.left = `${person.pct_x}%`;
      pin.style.top = `${person.pct_y}%`;
      pin.style.width = `${person.pct_r * 2.4}%`;
      pin.style.height = `${person.pct_r * 2.4 * 1.34}%`; // aspect ratio adjustment

      // Tooltip
      const tooltip = document.createElement("div");
      tooltip.className = "face-tooltip";
      tooltip.innerHTML = `
        <div class="tooltip-name">${person.name}</div>
        <div class="tooltip-row">${person.row} • #${person.pos}</div>
      `;
      pin.appendChild(tooltip);

      // Pin interactions
      pin.addEventListener("mouseenter", () => this.highlightPerson(person.id, true));
      pin.addEventListener("mouseleave", () => this.highlightPerson(person.id, false));
      pin.addEventListener("click", (e) => {
        e.stopPropagation();
        if (this.calibrationMode) {
          this.setCalibratingPerson(person);
        } else {
          this.openModal(person);
        }
      });

      this.hotspotsLayer.appendChild(pin);
    });
  }

  /* Filter Roster & Render Cards */
  filterAndRender() {
    this.filteredRoster = this.roster.filter(p => {
      const matchesFilter = (this.activeFilter === "all") || (p.category === this.activeFilter);
      const matchesSearch = !this.searchQuery || 
        p.name.toLowerCase().includes(this.searchQuery) ||
        p.role.toLowerCase().includes(this.searchQuery) ||
        p.row.toLowerCase().includes(this.searchQuery);
      return matchesFilter && matchesSearch;
    });

    this.rosterCountBadge.textContent = `${this.filteredRoster.length} members`;
    this.selectedSummary.textContent = this.searchQuery 
      ? `Found ${this.filteredRoster.length} matches for "${this.searchQuery}"`
      : `Showing ${this.filteredRoster.length} of ${this.roster.length} members`;

    // Highlight or dim pins on photo according to search
    const matchingIds = new Set(this.filteredRoster.map(p => p.id));
    this.roster.forEach(p => {
      const pin = document.getElementById(`pin-${p.id}`);
      if (!pin) return;
      if (matchingIds.has(p.id)) {
        pin.classList.remove("dimmed");
        if (this.searchQuery) pin.classList.add("highlighted");
        else pin.classList.remove("highlighted");
      } else {
        pin.classList.add("dimmed");
        pin.classList.remove("highlighted");
      }
    });

    this.renderRoster();
  }

  renderRoster() {
    this.alumniGrid.innerHTML = "";

    if (this.filteredRoster.length === 0) {
      this.alumniGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">
          No batchmate or professor found matching "${this.searchQuery}". Try another spelling.
        </div>
      `;
      return;
    }

    this.filteredRoster.forEach(person => {
      const card = document.createElement("div");
      card.className = "alumni-card";
      card.id = `card-${person.id}`;
      card.dataset.id = person.id;

      const update = this.profileUpdates[person.id] || {};
      const hasUpdateBadge = update.city || update.role ? "⭐ Updated" : "";

      card.innerHTML = `
        <img class="card-avatar" src="assets/avatars/${person.id}.jpg" alt="${person.name}" loading="lazy" onerror="this.src='assets/photo_deskewed.jpg'">
        <div class="card-content">
          <div class="card-name" title="${person.name}">${person.name}</div>
          <div class="card-row">${person.row} • #${person.pos}</div>
          <div>
            <span class="card-role-tag ${person.category === 'sitting' ? 'faculty' : ''}">${person.role}</span>
            ${hasUpdateBadge ? `<span class="card-role-tag" style="background:#2a452c; color:#85e89d;">${hasUpdateBadge}</span>` : ''}
          </div>
        </div>
        <div class="card-action-hint">Click to View &rarr;</div>
      `;

      card.addEventListener("mouseenter", () => this.highlightPerson(person.id, true));
      card.addEventListener("mouseleave", () => this.highlightPerson(person.id, false));
      card.addEventListener("click", () => this.openModal(person));

      this.alumniGrid.appendChild(card);
    });
  }

  /* Dual Highlighting (Face Pin <-> Roster Card) */
  highlightPerson(personId, isHovered) {
    const pin = document.getElementById(`pin-${personId}`);
    const card = document.getElementById(`card-${personId}`);

    if (isHovered) {
      if (pin) pin.classList.add("highlighted");
      if (card) {
        card.classList.add("highlighted");
      }
    } else {
      if (!this.searchQuery && pin) pin.classList.remove("highlighted");
      if (card) card.classList.remove("highlighted");
    }
  }

  /* Spotlight & Pan into Center View */
  spotlightPerson(personId) {
    const person = this.roster.find(p => p.id === personId);
    if (!person) return;

    // Set scale and pan centered on this face
    this.scale = 2.4;

    const imgW = this.mainPhoto.clientWidth || 1000;
    const imgH = this.mainPhoto.clientHeight || 740;

    const targetX = (person.pct_x / 100.0) * imgW;
    const targetY = (person.pct_y / 100.0) * imgH;

    const centerX = imgW / 2;
    const centerY = imgH / 2;

    this.panX = -((targetX - centerX) * this.scale);
    this.panY = -((targetY - centerY) * this.scale);
    this.updateTransform();

    // Pulse pin
    const pin = document.getElementById(`pin-${person.id}`);
    if (pin) {
      pin.classList.add("active-selected");
      setTimeout(() => pin.classList.remove("active-selected"), 3500);
    }

    // Scroll viewport into view if on mobile
    this.viewport.scrollIntoView({ behavior: "smooth", block: "center" });
    this.showToast(`Spotlighted: ${person.name}`);
  }

  /* Alumni Profile Modal ("Then & Now") */
  openModal(person) {
    this.selectedPerson = person;
    this.modalName.textContent = person.name;
    this.modalRowRole.textContent = `${person.row} • Position #${person.pos} • ${person.role}`;
    this.modalAvatar1991.src = `assets/avatars/${person.id}.jpg`;

    // Load saved updates if any
    const update = this.profileUpdates[person.id] || {};
    this.profileCity.value = update.city || "";
    this.profileRole.value = update.currentRole || "";
    this.profileContact.value = update.contact || "";
    this.profileNickname.value = update.nickname || "";
    this.profileMemory.value = update.memory || "";

    if (update.currentPhoto) {
      this.modalAvatarCurrent.src = update.currentPhoto;
      this.modalAvatarCurrent.style.display = "block";
      this.uploadPlaceholder.style.display = "none";
    } else {
      this.modalAvatarCurrent.src = "";
      this.modalAvatarCurrent.style.display = "none";
      this.uploadPlaceholder.style.display = "flex";
    }

    this.modalOverlay.classList.add("open");
  }

  closeModal() {
    this.modalOverlay.classList.remove("open");
  }

  handleCurrentPhotoUpload(e) {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const dataUrl = event.target.result;
      this.modalAvatarCurrent.src = dataUrl;
      this.modalAvatarCurrent.style.display = "block";
      this.uploadPlaceholder.style.display = "none";

      if (this.selectedPerson) {
        if (!this.profileUpdates[this.selectedPerson.id]) {
          this.profileUpdates[this.selectedPerson.id] = {};
        }
        this.profileUpdates[this.selectedPerson.id].currentPhoto = dataUrl;
      }
    };
    reader.readAsDataURL(file);
  }

  saveCurrentProfile() {
    if (!this.selectedPerson) return;
    const id = this.selectedPerson.id;

    if (!this.profileUpdates[id]) {
      this.profileUpdates[id] = {};
    }

    this.profileUpdates[id] = {
      ...this.profileUpdates[id],
      name: this.selectedPerson.name,
      row: this.selectedPerson.row,
      city: this.profileCity.value.trim(),
      currentRole: this.profileRole.value.trim(),
      contact: this.profileContact.value.trim(),
      nickname: this.profileNickname.value.trim(),
      memory: this.profileMemory.value.trim(),
      lastUpdated: new Date().toISOString()
    };

    this.saveLocalUpdates();
    this.showToast(`Saved profile update for ${this.selectedPerson.name}!`);
    this.renderRoster();
    this.closeModal();
  }

  exportUpdatesJSON() {
    const exportData = {
      batch: "GEC Raipur B.E. Mechanical 1990-91",
      exportedAt: new Date().toISOString(),
      profiles: this.profileUpdates
    };

    const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `gec_raipur_1991_batch_updates_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    this.showToast("Exported batch updates JSON file!");
  }

  /* Calibration Mode */
  toggleCalibrationMode(force) {
    this.calibrationMode = force !== undefined ? force : !this.calibrationMode;
    const hud = document.getElementById("calibrationHud");
    hud.style.display = this.calibrationMode ? "block" : "none";
    this.calibrateBtn.classList.toggle("active", this.calibrationMode);
    this.showToast(this.calibrationMode ? "Calibration mode enabled. Click a pin to adjust." : "Calibration mode disabled.");
  }

  setCalibratingPerson(person) {
    this.calibratingPerson = person;
    document.getElementById("activeCalibratePerson").textContent = `Selected: ${person.name} (${person.row})`;
  }

  copyCoordinatesJSON() {
    navigator.clipboard.writeText(JSON.stringify(this.roster, null, 2)).then(() => {
      this.showToast("Copied updated coordinates JSON to clipboard!");
    });
  }

  showToast(msg) {
    this.toastMsg.textContent = msg;
    this.toastMsg.classList.add("show");
    setTimeout(() => this.toastMsg.classList.remove("show"), 3200);
  }

  /* 35-Year Mechanical Engineering Ambient Reels & Milestones */
  async initAmbientReels() {
    if (!this.reelTrackLeft || !this.reelTrackRight) return;

    // Apply saved or default visibility
    if (this.stageMainArea) {
      this.stageMainArea.classList.toggle("reels-collapsed", !this.reelsVisible);
    }
    if (this.toggleReelsBtn) {
      this.toggleReelsBtn.classList.toggle("active", this.reelsVisible);
      this.toggleReelsBtn.addEventListener("click", () => {
        this.reelsVisible = !this.reelsVisible;
        this.stageMainArea.classList.toggle("reels-collapsed", !this.reelsVisible);
        this.toggleReelsBtn.classList.toggle("active", this.reelsVisible);
        try { localStorage.setItem("gec_reels_visible", this.reelsVisible); } catch (e) {}
        this.showToast(this.reelsVisible ? "35-Year Mechanical Reels visible" : "35-Year Mechanical Reels hidden");
      });
    }

    if (this.closeMilestoneModalBtn) {
      this.closeMilestoneModalBtn.addEventListener("click", () => this.closeMilestoneModal());
    }
    if (this.milestoneModalOverlay) {
      this.milestoneModalOverlay.addEventListener("click", (e) => {
        if (e.target === this.milestoneModalOverlay) this.closeMilestoneModal();
      });
    }

    // Load milestones dataset (from window.MILESTONES_DATA or fetch fallback)
    let milestones = window.MILESTONES_DATA;
    if (!milestones) {
      try {
        const res = await fetch("data/milestones.json");
        milestones = await res.json();
      } catch (err) {
        console.warn("Could not load milestones.json:", err);
      }
    }
    if (milestones && milestones.length) {
      this.milestones = milestones;
      this.renderMilestoneReels(milestones);
    }
  }

  renderMilestoneReels(milestones) {
    const foundations = milestones.filter(m => m.era.includes("Foundation"));
    const modern = milestones.filter(m => m.era.includes("Modern"));

    // Render left track (Foundations 1987-1991) - duplicated for seamless infinite drift
    const leftItems = [...foundations, ...foundations];
    this.reelTrackLeft.innerHTML = leftItems.map(m => this.createMilestoneCardHTML(m)).join("");

    // Render right track (Breakthroughs & Robotics 1991-2026) - duplicated for seamless drift
    const rightItems = [...modern, ...modern];
    this.reelTrackRight.innerHTML = rightItems.map(m => this.createMilestoneCardHTML(m)).join("");

    // Attach click listeners to cards
    document.querySelectorAll(".milestone-card").forEach(card => {
      card.addEventListener("click", () => {
        const id = card.dataset.id;
        const milestone = milestones.find(m => m.id === id);
        if (milestone) this.openMilestoneModal(milestone);
      });
    });
  }

  createMilestoneCardHTML(m) {
    return `
      <article class="milestone-card" data-id="${m.id}" title="${m.title}">
        <img class="milestone-card-img" src="${m.svg}" alt="${m.title}" loading="lazy">
        <div class="milestone-card-meta">
          <span>${m.year}</span>
          <span>${m.category}</span>
        </div>
        <div class="milestone-card-title">${m.title}</div>
        <div class="milestone-card-formula">${m.formula}</div>
      </article>
    `;
  }

  openMilestoneModal(m) {
    if (!this.milestoneModalOverlay) return;
    this.milestoneEraTag.textContent = m.era;
    this.milestoneModalTitle.textContent = m.title;
    this.milestoneModalCategory.textContent = `${m.category} • ${m.year}`;
    this.milestoneModalSvg.src = m.svg;
    this.milestoneModalSvg.alt = m.title;
    this.milestoneModalFormula.textContent = m.formula;
    this.milestoneModalDesc.textContent = m.description;
    this.milestoneModalMemory.textContent = `"${m.memory}"`;
    this.milestoneModalOverlay.classList.add("open");
  }

  closeMilestoneModal() {
    if (this.milestoneModalOverlay) {
      this.milestoneModalOverlay.classList.remove("open");
    }
  }
}

// Initialize on DOM load
window.addEventListener("DOMContentLoaded", () => {
  /* Appearance Mode Switcher (Blueprint, Heritage, Flow, Linen, Dark) */
  const THEME_KEY = "gec_theme_mode";
  function applyThemeMode(mode) {
    document.documentElement.setAttribute("data-theme-mode", mode);
    try { localStorage.setItem(THEME_KEY, mode); } catch (e) {}
    document.querySelectorAll(".appearance-pill").forEach((pill) => {
      pill.classList.toggle("active", pill.dataset.mode === mode);
    });
  }

  let savedMode = "blueprint";
  try { savedMode = localStorage.getItem(THEME_KEY) || "blueprint"; } catch (e) {}
  applyThemeMode(savedMode);

  document.addEventListener("click", (e) => {
    const pill = e.target.closest(".appearance-pill");
    if (!pill) return;
    applyThemeMode(pill.dataset.mode);
  });

  window.livingYearbook = new LivingYearbookApp();

  // Deep links from landing.html: index.html?q=Sinha or index.html#person=sit-15
  const app = window.livingYearbook;
  const params = new URLSearchParams(window.location.search);
  const query = params.get("q");
  if (query && app.searchInput) {
    app.searchInput.value = query;
    app.searchInput.dispatchEvent(new Event("input"));
  }
  const match = window.location.hash.match(/person=([\w-]+)/);
  if (match) {
    const runSpotlight = () => {
      app.spotlightPerson(match[1]);
      document.getElementById("viewport")?.scrollIntoView({ block: "center" });
    };
    if (app.mainPhoto && !app.mainPhoto.complete) {
      app.mainPhoto.addEventListener("load", runSpotlight, { once: true });
    } else {
      runSpotlight();
    }
  }
});
