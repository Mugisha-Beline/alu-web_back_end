import app from '../full_server/server.js';
import { use, request, expect } from 'chai';
import chaiHttp from 'chai-http';
process.argv[2] = './database.csv';

use(chaiHttp);

// Add console.log statements to debug file paths
console.log(require.resolve('../full_server/server.js'));
console.log(require.resolve('../full_server/controllers/StudentsController.js'));
console.log(require.resolve('../full_server/routes/index.js'));

describe('Server!', () => {
  it('welcomes user to the api', (done) => {
    request(app)
      .get('/students/CS')
      .end((err, res) => {
        if (err) {
          done(err);
          return;
        }
        expect(res).to.have.status(200);
        // Update the expected response based on the actual data from your database
        const expectedResponse =
          'List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie';
        expect(res.text).to.equals(expectedResponse);
        done();
      });
  });
});
