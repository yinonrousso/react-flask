import fetch from 'isomorphic-fetch';
import config from '../config/client';
import { responseHandler, requestError } from './common';

export const requestUsers = (params) => ({
  type: 'REQUEST_USERS', params
});

export const recieveUsers = (users) => ({
  type: 'RECIEVE_USERS', users
});

let getUsersURL = config.endpoint + 'users';

export function getUsers(params) {
  return (dispatch) => {
    dispatch(requestUsers(params));

    return fetch(getUsersURL).then(response => responseHandler(response)).then(json => {
      dispatch(recieveUsers(json));
    }).catch(err => {
      dispatch(requestError(err));
    });
  }
}
