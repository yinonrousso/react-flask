export const requestError = (error) => ({
  type: 'REQUEST_ERROR', error
});

export function responseHandler(response) {
  if (response.status >= 400) {
    return Promise.reject({msg: 'Status indicates error', status: response.status, response: response});
  } 
  return response.json();
}