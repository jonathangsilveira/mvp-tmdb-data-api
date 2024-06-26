from pydantic import BaseModel

class RateMoviePathModel(BaseModel):
    """
    Define contrato para caminho da rota de avaliação de filmes.

    Parâmetros:
        movie_id: ID do filme do TMDB API.
    """
    movie_id: int = 1022789

class RateMovieBodyModel(BaseModel):
    """
    Define contrato para avaliar um filme.

    Parâmetros:
        rate_value: Nota dada ao filme para avaliá-lo. Valores entre 0 e 10.
    """
    rate_value: int = 9

class AddToWatchlistPathModel(BaseModel):
    """
    Define contrato para adicionar um filme da lista para assistir.

    Parâmetros:
        watchlist: ID da watchlist.
        movie_id: ID do filme do TMDB API.
    """
    watchlist_id: int = 1
    movie_id: int = 1022789

class RemoveFromWatchlistPathModel(BaseModel):
    """
    Define contrato para remover um filme da lista para assistir.

    Parâmetros:
        watchlist: ID da watchlist.
        movie_id: ID do filme do TMDB API.
    """
    watchlist_id: int = 1
    movie_id: int = 1022789

class GetWatchlistQueryModel(BaseModel):
    """
    Define contrato para adicionar um filme da lista para assistir.

    Parâmetros:
        watchlist: ID da watchlist.
    """
    watchlist_id: int = 1

class WatchlistCreatedModel(BaseModel):
    """
    Define contrato para exibição da lista criada.

    Parâmetros:
        watchlist: ID da watchlist.
    """
    watchlist_id: int = 1

class WatchlistModel(BaseModel):
    """
    Define contrato para exibição de resultados da lista para assistir.

    Parâmetros:
        watchlist: ID da watchlist.
        movie_ids: Lista de IDs dos filmes registrados na lista para assistir.
    """
    watchlist_id: int
    movie_ids: list[int]

class SuccessModel(BaseModel):
    """
    Define contraro para exibição de resultado de sucesso padrão.
    """
    message: str = 'Operação concluída com sucesso!'

class ErrorModel(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    error_massage: str = "Erro ao adicionar filme na watchlist!"